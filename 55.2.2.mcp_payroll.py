import logging
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)

# Define MCP Server
mcp = FastMCP("Payroll-Server")

@mcp.tool()
def get_payslip_breakdown(date: str) -> str:
    """
    Retrieve a detailed breakdown of gross pay, taxes, and benefit deductions for a specific date.
    
    Args:
        date: The pay period date in YYYY-MM-DD format.
    """
    return f"Gross: $4,500 | Taxes: -$900 | 401k: -$200 | Net: $3,400 for {date}."

@mcp.tool()
def update_bank_details(account_number: str, routing_number: str, transit_number: str) -> str:
    """
    Update the direct deposit information for the employee's payroll.
    
    Args:
        account_number: The 6-digit bank account number
        routing_number: The 4-digit bank routing number.
        transit_number: The 3-digit bank transit number.
    """
    logging.info(f"Account number: {account_number}, Routing number: {routing_number}, Transit number: {transit_number}")
    
    return "Bank details updated. Changes will reflect in the next pay cycle."

@mcp.tool()
def generate_employment_letter(addressee: str) -> str:
    """
    Generate an official salary verification PDF for third-party entities (e.g., banks, landlords).
    
    Args:
        addressee: The name of the organization or individual requesting the verification.
    """
    return f"Letter generated for {addressee}. Download available in your portal."

if __name__ == "__main__":
    mcp.run(transport="http", port=8081)