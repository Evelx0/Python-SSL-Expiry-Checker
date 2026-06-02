import socket
import ssl
import datetime

# 1. Ask the user for the domain they want to check
domain = input("Enter a domain name to check (e.g., google.com): ")

# Clean up input (remove spaces, and strip http:// or https:// prefixes)
domain = domain.strip().lower()
if domain.startswith("https://"):
    domain = domain[8:]
elif domain.startswith("http://"):
    domain = domain[7:]
    
# Remove any trailing paths (e.g. google.com/search becomes google.com)
domain = domain.split("/")[0]

# Warning threshold (in days)
warning_days = 30

if not domain:
    print("Error: You did not enter a domain name.")
else:
    print(f"\nChecking SSL certificate for: {domain}...")
    
    try:
        # Create a default SSL context for verification
        context = ssl.create_default_context()
        
        # Connect to port 443 (HTTPS) with a 5-second timeout
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                
                # Get the certificate details
                cert = ssock.getpeercert()
                expiry_str = cert.get('notAfter')
                
                # Convert the expiration date string to a timestamp, then to a datetime object
                expiry_timestamp = ssl.cert_time_to_seconds(expiry_str)
                expiry_date = datetime.datetime.fromtimestamp(expiry_timestamp, tz=datetime.timezone.utc)
                
                # Calculate how many days are left until expiration
                now = datetime.datetime.now(datetime.timezone.utc)
                days_left = (expiry_date - now).days
                
                # Print the outcome
                print("\n--- RESULTS ---")
                print(f"Expiration Date: {expiry_str}")
                
                if days_left < 0:
                    print(f"Status: EXPIRED! (Expired {-days_left} days ago)")
                elif days_left <= warning_days:
                    print(f"Status: WARNING! Expiring soon. Only {days_left} days left.")
                else:
                    print(f"Status: OK. The certificate is valid ({days_left} days left).")
                    
    except Exception as e:
        # Catch errors such as DNS failure or connection timeout
        print(f"\nError: Could not check certificate. Reason: {e}")
