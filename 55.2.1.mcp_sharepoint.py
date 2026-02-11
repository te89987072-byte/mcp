import random
import logging
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)

# Define MCP Server
mcp = FastMCP("SharePoint-Server")

@mcp.tool()
def check_permissions(site_url: str, user_email: str) -> str:
    """
    Verify the current access level for a specific user on a SharePoint site.
    """
    # Simulate logic
    result = f"User {user_email} currently has 'Read' access to {site_url}."
    logging.info(f"Result: {result}")

    return result

@mcp.tool()
def grant_permission(site_url: str, user_email: str, permission_level: str = "Read") -> str:
    """
    Grant a user specific access permissions to a SharePoint site.
    
    Args:
        site_url: The full URL of the target SharePoint site.
        user_email: The corporate email address of the recipient.
        permission_level: The level of access to grant. Must be 'Read', 'Contribute', or 'Full Control'.
    """
    result =  f"SUCCESS: Granted {permission_level} to {user_email} for {site_url}."
    logging.info(f"Result: {result}")

    return result

@mcp.tool()
def create_site_request(site_name: str, owner_alias: str, sensitivity_label: str) -> str:
    """
    Submit a formal request for a new SharePoint site provisioning.
    
    Args:
        site_name: The desired display name for the new site.
        owner_alias: The email or username of the primary site owner.
        sensitivity_label: The data classification. Must be 'Public', 'Internal', or 'Confidential'.
    """
    result =  f"Provisioning request for '{site_name}' created (Ticket #SHP-{random.randint(100,999)})."
    logging.info(f"Result: {result}")

    return result

@mcp.tool()
def get_site_usage(site_url: str) -> str:
    """
    Retrieve current storage metrics, quota limits, and health status for a site.
    
    Args:
        site_url: The full URL of the SharePoint site to analyze.
    """
    result =  "Usage: 9.5GB / 10GB. Site is approaching its storage limit."
    logging.info(f"Result: {result}")

    return result

@mcp.tool()
def increase_site_quota(site_url: str, amount_gb: int) -> str:
    """
    Increase the storage limit for a SharePoint site to prevent read-only locking.
    
    Args:
        site_url: The full URL of the site needing more space.
        amount_gb: The number of Gigabytes to add to the current quota.
    """
    result =  f"Quota for {site_url} increased by {amount_gb}GB."
    logging.info(f"Result: {result}")

    return result

if __name__ == "__main__":
    mcp.run(transport="http", port=8080)