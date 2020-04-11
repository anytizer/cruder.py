from flask import Flask

from apps import app_projects, app_terminations, app_artworks, app_customers, app_estimations, app_payments, \
    app_developers, app_works, app_info

import app_custom

app = Flask(__name__)
app.register_blueprint(app_artworks.bp)
app.register_blueprint(app_customers.bp)
app.register_blueprint(app_developers.bp)
app.register_blueprint(app_estimations.bp)
app.register_blueprint(app_payments.bp)
app.register_blueprint(app_projects.bp)
app.register_blueprint(app_terminations.bp)
app.register_blueprint(app_works.bp)
app.register_blueprint(app_info.bp)

# DO NOT EDIT BELOW
app.register_blueprint(app_custom.bp)

# /export/table
# /import

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
