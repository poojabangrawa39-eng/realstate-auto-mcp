
import os
import json
import urllib.request
import urllib.error
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("MyFirstMCP")


@mcp.tool()
def send_lead_to_n8n(
    Campaign: str,
    CustomerType: str,
    CustomerSubType: str,
    customerName: str,
    ContactNumber: str,
    Email: str,
    city: str,
    location: str,
    sublocation: str,
    GoogleMap: str,
    AgeOfProperty: str,
    Area: str,
    Price: str,
    Adderess: str,
    PropertyDetails: str,
    Facillities: str,
    TotalUnits: str,
    Dates: str,
    ReferenceId: str,
    Description: str,
    WebsiteURL: str,
    CreatedDate: str,
    UpdatedDate: str
) -> str:
    """Send real-estate CRM data to n8n and return the response."""

    webhook_url = "https://automation.ibigdata.in/webhook/realestate-data"

    payload = {
        "Campaign": Campaign,
        "CustomerType": CustomerType,
        "CustomerSubType": CustomerSubType,
        "customerName": customerName,
        "ContactNumber": ContactNumber,
        "Email": Email,
        "city": city,
        "location": location,
        "sublocation": sublocation,
        "GoogleMap": GoogleMap,
        "AgeOfProperty": AgeOfProperty,
        "Area": Area,
        "Price": Price,
        "Adderess": Adderess,
        "PropertyDetails": PropertyDetails,
        "Facillities": Facillities,
        "TotalUnits": TotalUnits,
        "Dates": Dates,
        "ReferenceId": ReferenceId,
        "Description": Description,
        "WebsiteURL": WebsiteURL,
        "CreatedDate": CreatedDate,
        "UpdatedDate": UpdatedDate
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            response_body = response.read().decode("utf-8")
            return (
                f"HTTP Status: {response.status}\n"
                f"n8n Response: {response_body}"
            )

    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8", errors="replace")
        return f"HTTP Error {error.code}: {error_body}"

    except Exception as error:
        return f"Request failed: {type(error).__name__}: {error}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
