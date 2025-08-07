# access-certification-campaign-tool

# Abstract

Access Certification Campaign Tool is a web-based Identity Governance and Administration (IGA) platform built with Django and PostgreSQL, designed to help organizations perform regular access reviews for compliance. It integrates with LDAP for authentication and uses a SCIM 2.0 connector to fetch users and roles from identity providers like Okta or Azure AD. The tool enables administrators to launch campaigns, and managers to certify or revoke user access to applications and roles, with audit-ready reporting capabilities.

A secure and extensible Access Review Platform built with Django + PostgreSQL, featuring:

1. LDAP integration for enterprise authentication

2. SCIM 2.0 connector for user and access provisioning

3. Web-based campaign management for access certifications

4. Exportable reports for audit compliance


Features
1. Campaign Creation: Easily create access review campaigns from imported user/access data.

2. SCIM 2.0 Support: Pull users and groups from identity providers like Okta or Azure AD.

3. LDAP Authentication: Login using Active Directory or OpenLDAP.

4. Access Reviews: Let managers review and approve/revoke access to applications and roles.

5. Admin Dashboard: Built-in Django admin for campaign oversight.

6. CSV Loader: Import users and access entries from CSV files using custom Django commands.

7. Export Reports: Download campaign results in CSV format for audits.

Use Cases
1. Identity and Access Management (IAM)

2. Compliance audits (e.g., SOX, ISO 27001)

3. Quarterly Access Reviews (QAR)

Enterprise user provisioning and governance

