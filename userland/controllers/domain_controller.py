from flask_cors import cross_origin
from flask_login import current_user, login_required
from application.userland.controller import mod_userland
from flask import request, abort, render_template, redirect, current_app
from application.core.utils.domain_utils import DomainUtils


@mod_userland.route('/home', methods=['GET', 'POST'])
@login_required
def get_search_detail_domain():
    keyword = request.form.get('keyword')
    if keyword:
        response = DomainUtils.get_search_domain(keyword)
    else:
        abort(500, 'keyword is not found.')

    return response


@mod_userland.route('/delete', methods=['GET', 'POST'])
def delete_domain():
    domains = request.args.get('keyword')
    key = request.args.get('keyword')
    print(domains)
    if domains:
        response = DomainUtils.delete_selected_domains(domains)
    else:
        abort(500, 'responses is not deleted.')
    return render_template('result.html', response=response)
