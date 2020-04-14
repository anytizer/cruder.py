import os

import meta
from meta import encrypt


def routes_body(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    lookups = "".join([f"""
        kv_{h['column']}s_sql = "{h['sql']}"
        {h['column']}s = entity.query(kv_{h['column']}s_sql, ())
    """ for h in hidden])
    lookups_assignments = ", ".join([f"{h['column']}s={h['column']}s" for h in hidden])

    routes = meta.ts("ts/app.ts")
    routes = routes.replace("{table}", table)
    routes = routes.replace("{pk_id}", pk_id)
    routes = routes.replace("{LOOKUPS}", "".join(lookups))
    routes = routes.replace("{LOOKUPS_ASSIGNMENTS}", lookups_assignments)
    meta.write(f"apps/app_{table}.py", routes)


def entity_body(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    def _insert(columns=()) -> str:
        insert_fields = ", ".join([f"`{field}`" for field in columns])
        insert_data = ", ".join([f":{encrypt(field)}" for field in columns])

        insert_sql = f"""
            INSERT INTO `{table}` (
                {insert_fields}
            ) VALUES(
                {insert_data}
            );"""
        return insert_sql

    def _update(columns=()):
        update_fields = ", ".join([f"`{field}`=:{encrypt(field)}" for field in columns])
        update_sql = f"""UPDATE `{table}` SET {update_fields} WHERE `{pk_id}`=:{pk_id};"""
        return update_sql

    insert_query = _insert(columns)
    update_query = _update(columns)

    entity_template = meta.ts("ts/entity.ts")
    entity_template = entity_template.replace("{table}", table)
    entity_template = entity_template.replace("{pk_id}", pk_id)
    entity_template = entity_template.replace("{insert_query}", insert_query)
    entity_template = entity_template.replace("{update_query}", update_query)
    meta.write(f"entities/entity_{table}.py", entity_template)


def list_form(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    columns = [column for column in columns if not column == "id"]
    columns = [column for column in columns if not column.endswith("_id")]
    columns = [column for column in columns if not column.endswith("_active")]
    columns = [column for column in columns if not column.endswith("_password")]
    columns = [column for column in columns if not column.endswith("_code")]

    __THEADS__ = "\r\n    ".join([f"<th>{meta.headname(field, prefix)}</th>" for field in columns])
    __THEADS__EXTRAS__ = "\r\n    ".join([f"<th>{meta.headname(field['column'], prefix)}</th>" for field in extras])
    __THEADS__ = __THEADS__ + __THEADS__EXTRAS__

    tbody = "".join([f"""<td>{{{{ d.{field} }}}}</td>""" for field in columns])
    TBODY_EXTRAS = "".join([f"<td><a href='{field['url'].replace('/<>', '')}/{{{{ d.{pk_id} }}}}'>{field['column']}</td>" for field in extras])
    tbody = tbody + TBODY_EXTRAS

    list_html = meta.ts("ts/list.ts")
    list_html = list_html.replace("{table}", table)
    list_html = list_html.replace("{pk_id}", pk_id)
    list_html = list_html.replace("__THEADS__", __THEADS__)
    list_html = list_html.replace("__TBODY__", tbody)
    meta.write(f"templates/{table}/list.html", list_html)


def add_form(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    columns = [column for column in columns if not column.endswith("_id")]
    # columns = [column for column in columns if not column.endswith("_active")]
    # columns = [column for column in columns if not column.endswith("_password")]

    htmls_add = "".join([f"""
        <div class='w3-row w3-padding'>
            <div class='w3-col l2'><label for='f_{field}'>{meta.headname(field)}</label></div>
            <div class='w3-col l10'><input type='text' id='f_{field}' name='{meta.encrypt(field)}' value='' placeholder='{field}' /></div>
        </div>
    """ for field in columns])

    __foreign__ = "".join([f"""

<div class='w3-row w3-padding'>
    <div class='w3-col l2'>{meta.headname(h['column'])}</div>
    <div class='w3-col l10'>
        <select name="{h['column']}"><option value=""></option>
            {{% for k, v in {h['column']}s %}}<option value="{{{{ k }}}}">{{{{ v }}}}</option>{{% endfor %}}
        </select>
    </div>
</div>
    """ for h in hidden])

    add_form_html = meta.ts("ts/add.ts")
    add_form_html = add_form_html.replace("{table}", table)
    add_form_html = add_form_html.replace("{pk_id}", pk_id)
    add_form_html = add_form_html.replace("{__htmls_add__}", htmls_add)
    add_form_html = add_form_html.replace("{__foreign__}", __foreign__)

    meta.write(f"templates/{table}/add.html", add_form_html)


def edit_form(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    columns = [column for column in columns if not column.endswith("_id")]
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


def details_form(table="", columns=(), prefix="", hidden=(), extras=(), pk_id=""):
    columns = [column for column in columns if not column.endswith("_id")]
    columns = [column for column in columns if not column.endswith("_active")]
    columns = [column for column in columns if not column.endswith("_password")]

    detail_fields = "".join([f"""
        <div class='w3-row w3-padding'>
            <div class='w3-col l2'>{meta.headname(field)}</div>
            <div class='w3-col l10'>{{{{ data.{field} }}}}</div>
        </div>
        """ for field in columns])
    detail_extras = ""
    if extras:
        detail_extras = " | ".join([meta.href(table, field, pk_id) for field in extras])

    details_html = meta.ts("ts/details.ts")
    details_html = details_html.replace("{table}", table)
    details_html = details_html.replace("{pk_id}", pk_id)
    details_html = details_html.replace("{detail_fields}", detail_fields)
    details_html = details_html.replace("{detail_extras}", detail_extras)
    meta.write(f"templates/{table}/details.html", details_html)


from config import cruds

inc_menu_html = " | ".join([f"<a href='/{table}/list'>{name}</a>" for table, prefix, name, hidden, extras in cruds])
inc_menu_html += " | <a href='/reports/reports'>Report</a>"
meta.write("templates/inc.menus.html", inc_menu_html)

meta.write("templates/base.html", meta.ts("ts/base.ts"))
for table, prefix, name, hidden, extras in cruds:
    os.makedirs(f"templates/{table}/", 0x777, True)
    os.makedirs(f"entities/", 0x777, True)
    os.makedirs(f"apps/", 0x777, True)

    pk_id = meta.pk(table)
    columns = meta.columns(table)

    entity_body(table, columns, prefix, hidden, extras, pk_id)
    routes_body(table, columns, prefix, hidden, extras, pk_id)
    list_form(table, columns, prefix, hidden, extras, pk_id)
    add_form(table, columns, prefix, hidden, extras, pk_id)
    edit_form(table, columns, prefix, hidden, extras, pk_id)
    details_form(table, columns, prefix, hidden, extras, pk_id)
    print(f"app.register_blueprint(app_{table}.bp)")
print(f"# www.py: Register your BluePrint (app_{table}) in www.py")
