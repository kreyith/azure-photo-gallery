Azure Photo Gallery

A cloud-based photo gallery application built on Microsoft Azure.  
Demonstrates cloud infrastructure, storage, authentication, and monitoring.

---

Architecture Overview

![Architecture Diagram](diagrams/architecture.png) - fake link for now

- **Front End**: [Your tech choice: Flask, React, or Static Web App]  
- **Authentication**: Azure AD B2C (user sign-up/sign-in)  
- **Storage**: Azure Blob Storage for photos  
- **Database**: Azure SQL Database for metadata (photo info, uploader, timestamp)  
- **Optional**: Azure Function for image resizing/thumbnails  
- **Security**: Azure Key Vault for secrets, NSGs, RBAC for access control  
- **Monitoring**: Azure Monitor + Log Analytics for metrics and logs  

---

Features

- Upload and view photos from a web front end  
- Metadata stored securely in Azure SQL Database  
- Authentication with Azure AD B2C (admin vs regular users)  
- Secure configuration using Key Vault + private endpoints  
- Logging and monitoring via Azure Monitor  

---

 Deployment Instructions

### 1. Manual Deployment
1. Create a Resource Group in Azure.  
2. Deploy Blob Storage, SQL Database, and App Service.  
3. Configure Azure AD B2C for sign-up/sign-in flow.  
4. Connect App Service to Blob + SQL (using Key Vault for secrets).  

### 2. Infrastructure-as-Code (Terraform/Bicep)
```bash
# Example Terraform commands
terraform init
terraform plan
terraform apply
