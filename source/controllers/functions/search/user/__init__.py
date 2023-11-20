from flask import Blueprint, request
from flask_login import login_required
from source.controllers.functions.search.user.function import _process_search_user

search_user = Blueprint(name='search_user', import_name=__name__)

@search_user.route('/users', methods=['POST', 'GET'])
@login_required
def searchuser():
    get_keyword = request.args.get('keyword')
    get_filter = request.args.get('filter')
    get_sort = request.args.get('sort')
    if get_keyword == '' or get_keyword == None:
        return 'CTF_IA17A{sql4lch3my_1nj3c7373d}' + '<br>' + 'CTF_IA17A{sqlalchemy_injected}' + '<br>' + 'éo hiểu sao keyword='' là hắn trả về hết dữ liệu luôn :D' + '<br>' + '<img src="../static/Server/resources/error/Screenshot_2023-11-05_20_33_20.png">' + '<br>' + '<img src="../static/Server/resources/error/Screenshot_2023-11-05_20_33_34.png">'
    elif get_filter not in ['username', 'firstname', 'first_name', 'first name', 'lastname', 'last_name', 'last name', 'phone', 'email', 'address', 'career'] or get_sort not in ['increase', 'decrease', 'asc', 'desc']:
        return 'CTF_IA17A{c0n9r4t3_y0ur_f1r5t_try}' + '<br>' + 'sửa các option filter là web t hắn lỗi liền'
    else:
        return _process_search_user(get_keyword, get_filter, get_sort)