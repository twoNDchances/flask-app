from flask import Blueprint, request
from flask_login import login_required
from source.controllers.functions.search.book.function import _process_search_book

search_book = Blueprint(name='search_book', import_name=__name__)

@search_book.route('/books', methods=['POST', 'GET'])
@login_required
def search():
    get_keyword = request.args.get('keyword')
    get_filter = request.args.get('filter')
    get_sort = request.args.get('sort')
    get_show = request.args.get('show')
    if get_keyword == '' or get_keyword == None:
        return 'CTF_IA17A{sql4lch3my_1nj3c7373d}' + '<br>' + 'CTF_IA17A{sqlalchemy_injected}' + '<br>' + 'éo hiểu sao keyword='' là hắn trả về hết dữ liệu luôn :D' + '<br>' + '<img src="../static/Server/resources/error/Screenshot_2023-11-05_20_33_20.png">' + '<br>' + '<img src="../static/Server/resources/error/Screenshot_2023-11-05_20_33_34.png">'
    elif get_filter not in ['title', 'author', 'release_year', 'release year', 'releaseyear'] or get_sort not in ['increase', 'decrease', 'asc', 'desc'] or get_show not in ['card', 'table']:
        return 'CTF_IA17A{c0n9r473_y0ur_f1r57_7ry}' + '<br>' + 'CTF_IA17A{congrate_your_first_try}' + '<br>' + 'sửa các option filter là web t hắn lỗi liền'
    elif get_filter == 'release_year' and not get_keyword.isdigit():
        return 'CTF_IA17A{1n7393r_15_d4n93r0u5}' + '<br>' + 'CTF_IA17A{integer_is_dangerous}' + '<br>' + 'search khác số nguyên như lại filter theo integer'
    else:
        return _process_search_book(get_keyword, get_filter, get_sort, get_show)
