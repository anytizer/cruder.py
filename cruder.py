import os

import meta
from meta import encrypt


def routes_body(table="", columns="", prefix=""):
    routes = meta.ts("ts/app.ts")
    routes = routes.replace("{table}", table)
    routes = routes.replace("{pk_id}", pk_id)
    meta.write(f"apps/app_{table}.py", routes)


def entity_body(table="", columns="", prefix=""):
    def _insert(columns=[]):
        insert_fields = ", ".join([f"`{field}`" for field in columns])
        insert_data = ", ".join([f":{encrypt(field)}" for field in columns])

        insert_sql = f"""
            INSERT INTO `{table}` (
                {insert_fields}
            ) VALUES(
                {insert_data}
            );"""
        return insert_sql

    def _update(columns=[]):
        update_fields = ", ".join([f"`{field}`=:{encrypt(field)}" for field in columns])
        update_sql = f"""UPDATE `{table}` SET {update_fields} WHERE `{pk_id}`=:{pk_id};"""
        return update_sql

    def _data(columns=[]):
        return "FIELD TO REPLACE"

    insert_query = _insert(columns)
    update_query = _update(columns)
    __DATA__ = _data(columns)

    entity_template = meta.ts("ts/entity.ts")
    entity_template = entity_template.replace("{DATA_COLUMNS_VALUES}", __DATA__)
    entity_template = entity_template.replace("{table}", table)
    entity_template = entity_template.replace("{pk_id}", pk_id)
    entity_template = entity_template.replace("{insert_query}", insert_query)
    entity_template = entity_template.replace("{update_query}", update_query)
    meta.write(f"entities/entity_{table}.py", entity_template)


def list_form(table="", columns="", prefix=""):
    columns = [column for column in columns if not column.endswith("_id")]
    columns = [column for column in columns if not column.endswith("_active")]
    columns = [column for column in columns if not column.endswith("_password")]

    __THEADS__ = "\r\n    ".join([f"<th>{meta.headname(field, prefix)}</th>" for field in columns])

    tbody = ""
    for field in columns:
        tbody = tbody + f"""
        <td>{{{{ d.{field}}}}}</td>
"""
    list_html = meta.ts("ts/list.ts")
    list_html = list_html.replace("{table}", table)
    list_html = list_html.replace("{pk_id}", pk_id)
    list_html = list_html.replace("__THEADS__", __THEADS__)
    list_html = list_html.replace("__TBODY__", tbody)
    meta.write(f"templates/{table}/list.html", list_html)


def add_form(table="", columns=[], prefix="", hidden=[]):
    pk_id = meta.pk(table)
    columns = [column for column in columns if not column.endswith("_id")]
    # columns = [column for column in columns if not column.endswith("_active")]
    # columns = [column for column in columns if not column.endswith("_password")]

    htmls_add = "".join([f"""
        <div class='w3-row w3-padding'>
            <div class='w3-col l2'><label for='f_{field}'>{meta.headname(field)}</label></div>
            <div class='w3-col l10'><input type='text' id='f_{field}' name='{encrypt(field)}' value='' placeholder='{field}' /></div>
        </div>
    """ for field in columns])

    hidden_fields = "".join([f"<input type='hidden' name='{h}' value='' />" for h in hidden])

    # import meta
    add_form_html = meta.ts("ts/add.ts")
    add_form_html = add_form_html.replace("{table}", table)
    add_form_html = add_form_html.replace("{pk_id}", pk_id)
    add_form_html = add_form_html.replace("{htmls_add}", htmls_add)
    add_form_html = add_form_html.replace("{hidden}", hidden_fields)
    # return add_form_html

    meta.write(f"templates/{table}/add.html", add_form_html)


def edit_form(table="", columns=[], prefix=""):
    htmls_edit = "".join([f"""
        <div class='w3-padding w3-row'>
            <div class='w3-col l2'><label for='f_{field}'>{meta.headname(field)}</label></div>
            <div class='w3-col l2'><input type='text' id='f_{field}' name='{meta.encrypt(field)}' value='{{{{ data.{field} }}}}' /></div>
        </div>
    """ for field in columns])
    edit_html = meta.ts("ts/edit.ts")
    edit_html = edit_html.replace("{table}", table)
    edit_html = edit_html.replace("{pk_id}", pk_id)
    edit_html = edit_html.replace("{htmls_edit}", htmls_edit)
    meta.write(f"templates/{table}/edit.html", edit_html)


def details_form(table="", columns=[], prefix=""):
    columns = [column for column in columns if not column.endswith("_id")]
    columns = [column for column in columns if not column.endswith("_active")]
    columns = [column for column in columns if not column.endswith("_password")]

    detail_fields = "".join([f"""
        <div class='w3-row w3-padding'>
            <div class='w3-col l2'>{meta.headname(field)}</div>
            <div class='w3-col l10'>{{{{ data.{field} }}}}</div>
        </div>
        """ for field in columns])
    details_html = meta.ts("ts/details.ts")
    details_html = details_html.replace("{table}", table)
    details_html = details_html.replace("{pk_id}", pk_id)
    details_html = details_html.replace("{detail_fields}", detail_fields)
    meta.write(f"templates/{table}/details.html", details_html)


from config import cruds

inc_menu_html = " | ".join([f"<a href='/{table}/list'>{name}</a>" for table, prefix, name, hidden, flags in cruds])
meta.write("templates/inc.menus.html", inc_menu_html)

meta.write("templates/base.html", meta.ts("ts/base.ts"))
for table, prefix, name, hidden, flags in cruds:
    pk_id = meta.pk(table)
    columns = meta.columns(table)

    os.makedirs(f"templates/{table}/", 0x777, True)

    entity_body(table, columns, prefix)
    routes_body(table, columns, prefix)
    list_form(table, columns, prefix)
    add_form(table, columns, prefix, hidden)
    edit_form(table, columns, prefix)
    details_form(table, columns, prefix)
    # print(f"Register your BluePrint (app_{table}) in www.py")
    print(f"app.register_blueprint(app_{table}.bp)")
print("# www.py")
