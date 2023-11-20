from datetime import datetime
from os import path
from flask import flash, redirect, render_template, session, url_for
from pdf2image import convert_from_path
from source import database
from source.controllers.functions.search.form import SearchForm
from source.controllers.functions.create.book.form import UploadForm
from source.controllers.processor.crypto import generate_secret_key_64
from source.controllers.processor.queries import _query_object_book_by_query, _query_user_id_by_username
from source.datatable import Book, Image
from werkzeug.utils import secure_filename

def _process_add():
    form_search = SearchForm()
    if form_search.validate_on_submit():
        keyword = form_search.keyword.data
        return redirect(url_for('search.search_book.search', keyword=keyword, filter='title', sort='increase', show='table'))
    form = UploadForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        release_year = form.release_year.data
        files = form.file.data
        file_name = secure_filename(files.filename)
        pdf_storage_path = str(path.join(r'/var/www/flask-app/source/static/{username}/books'.format(username=session['username']), file_name))
        new_book = Book(
                title=title,
                author=author,
                release_year=release_year, created_at=datetime.now(),
                book=pdf_storage_path, user_id=_query_user_id_by_username(username=session['username']),
                key=generate_secret_key_64()
            )
        database.session.add(new_book)
        database.session.commit()
        files.save(pdf_storage_path)
        ############################################################################
        book_id = _query_object_book_by_query()[-1].id
        get_image_from_pdf = convert_from_path(pdf_path=pdf_storage_path, dpi=50)
        image_storage_path = r'/var/www/flask-app/source/static/{username}/images/'.format(username=session['username'])
        filename_without_extension = path.splitext(file_name)[0]
        full_path = path.join(image_storage_path, str(filename_without_extension) + '.jpg')
        get_image_from_pdf[0].save(full_path)
        new_image = Image(path=full_path, book_id=book_id)
        database.session.add(new_image)
        database.session.commit()
        flash('Upload Successful', 'success')
        # session['is_available'] = False
        # for file in files:
        #     file_name = secure_filename(file.filename)
        #     if file_name.endswith('.pdf'):
        #         file.save(path.join(pdf_storage_path, file_name))
        #         session['message'] = 'Upload successfully!'
        #     else:
        #         session['message'] = 'Your file list contains non-pdf files, which have been automatically deleted'
        return redirect(url_for('list.list.library', page=1))
    return render_template(template_name_or_list='add.html', form=form, form_search=form_search)
