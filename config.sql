DROP TABLE IF EXISTS config_tables;
CREATE TABLE "config_tables" (
    "table_id"	TEXT NOT NULL,
    "table_name"	TEXT NOT NULL,
    "table_prefix" TEXT NOT NULL,
    "pk_column" TEXT NOT NULL,
    "hidden_columns" TEXT NOT NULL,
    "extra_columns" TEXT NOT NULL,
    "do_crud"  TEXT NOT NULL,
    "parent_column" TEXT NOT NULL,
    UNIQUE("table_name"),
    PRIMARY KEY("table_id")
);

DROP TABLE IF EXISTS config_showfields;
CREATE TABLE "config_showfields" (
    "config_id"	TEXT NOT NULL,
    "table_id"	TEXT NOT NULL,
    "column_name"	TEXT NOT NULL,
    "display_name"	TEXT NOT NULL,
    "display_order"	TEXT NOT NULL,
    "column_datatype"	TEXT NOT NULL,
    "showon_list"	TEXT NOT NULL,
    "showon_edit"	TEXT NOT NULL,
    "showon_detail"	TEXT NOT NULL,
    "showon_insert"	TEXT NOT NULL,
    "reserved_field"	TEXT NOT NULL,
    FOREIGN KEY("table_id") REFERENCES "config_tables"("table_id") ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE("table_id","column_name"),
    PRIMARY KEY("config_id")
);

DROP TABLE IF EXISTS config_colors;
CREATE TABLE "config_colors" (
    "config_id"	TEXT NOT NULL,
    "table_id"	TEXT NOT NULL,
    "column_name"	TEXT NOT NULL,
    "color_back"	TEXT NOT NULL,
    "color_front"	TEXT NOT NULL,
    "color_hover"	TEXT NOT NULL,
    FOREIGN KEY("table_id") REFERENCES "config_tables"("table_id") ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE("table_id","column_name"),
    PRIMARY KEY("config_id")
);