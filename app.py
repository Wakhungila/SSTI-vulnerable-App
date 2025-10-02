from flask import Flask, render_template

# Import all lesson Blueprints
from lessons import (
    sqli_basic, xss_reflected, ssti, auth_broken_login, file_upload, xxe, ssrf_basic, register,
    race_condition, business_logic, upload_chain, api_idor, graphql_idor,
    ssrf_metadata, upload_xss_chain, graphql_bola,
    sqli_rce_chain, graphql_jwt_chain,
    csrf_2fa_bypass, api_chain_escalation, oauth_misconfig,
    bac_upload_rce, jwt_none_chain
)

app = Flask(__name__)
app.secret_key = 'vulnlab_secret'

# Register Blueprints for all lessons
app.register_blueprint(sqli_basic.sqli_bp)
app.register_blueprint(xss_reflected.xss_bp)
app.register_blueprint(ssti.ssti_bp)
app.register_blueprint(auth_broken_login.auth_bp)
app.register_blueprint(file_upload.file_upload_bp)
app.register_blueprint(xxe.xxe_bp)
app.register_blueprint(ssrf_basic.ssrf_bp)
app.register_blueprint(register.register_bp)

app.register_blueprint(race_condition.race_bp)
app.register_blueprint(business_logic.blf_bp)
app.register_blueprint(upload_chain.upload_chain_bp)
app.register_blueprint(api_idor.api_idor_bp)
app.register_blueprint(graphql_idor.graphql_idor_bp)

app.register_blueprint(ssrf_metadata.ssrf_metadata_bp)
app.register_blueprint(upload_xss_chain.upload_xss_bp)
app.register_blueprint(graphql_bola.graphql_bola_bp)

app.register_blueprint(sqli_rce_chain.sqli_rce_bp)
app.register_blueprint(graphql_jwt_chain.graphql_jwt_bp)

app.register_blueprint(csrf_2fa_bypass.csrf_2fa_bp)
app.register_blueprint(api_chain_escalation.api_chain_bp)
app.register_blueprint(oauth_misconfig.oauth_bp)

app.register_blueprint(bac_upload_rce.bac_rce_bp)
app.register_blueprint(jwt_none_chain.jwt_none_bp)

@app.route('/')
def home():
    lessons = [
        # Basic and intermediate labs
        {"name": "SQL Injection (Basic)", "url": "/lesson/sqli"},
        {"name": "Reflected XSS", "url": "/lesson/xss"},
        {"name": "Server-Side Template Injection (SSTI)", "url": "/lesson/ssti"},
        {"name": "Broken Authentication", "url": "/lesson/auth-broken"},
        {"name": "Unrestricted File Upload", "url": "/lesson/file-upload"},
        {"name": "XML External Entity (XXE)", "url": "/lesson/xxe"},
        {"name": "SSRF (Basic)", "url": "/lesson/ssrf"},
        {"name": "User Registration", "url": "/lesson/register"},
        {"name": "Race Condition: Double Withdrawal", "url": "/lesson/race"},
        {"name": "Business Logic Flaw: Discount Abuse", "url": "/lesson/business-logic"},
        {"name": "Multi-Step: File Upload & Path Traversal", "url": "/lesson/upload-chain"},
        {"name": "API IDOR (REST)", "url": "/lesson/api-idor"},
        {"name": "GraphQL IDOR", "url": "/lesson/graphql-idor"},
        # Advanced and chained labs
        {"name": "SSRF → Cloud Metadata Extraction", "url": "/lesson/ssrf-metadata"},
        {"name": "File Upload → Stored XSS", "url": "/lesson/upload-xss-chain"},
        {"name": "GraphQL BOLA (Broken Object Level Authorization)", "url": "/lesson/graphql-bola"},
        {"name": "SQLi → RCE Chain", "url": "/lesson/sqli-rce-chain"},
        {"name": "GraphQL + JWT Misconfig (Algorithm Confusion)", "url": "/lesson/graphql-jwt-chain"},
        {"name": "CSRF → 2FA Bypass", "url": "/lesson/csrf-2fa"},
        {"name": "API Chain: IDOR + Mass Assignment", "url": "/lesson/api-chain-escalation"},
        {"name": "OAuth Misconfig: Open Redirect & Scope Confusion", "url": "/lesson/oauth-misconfig"},
        {"name": "BAC → Insecure Upload → RCE Chain", "url": "/lesson/bac-upload-rce"},
        {"name": "JWT None Attack → Admin API Chain", "url": "/lesson/jwt-none-chain"},
    ]
    return render_template('lessons.html', lessons=lessons)

if __name__ == "__main__":
    app.run(debug=True)
