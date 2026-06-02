# Simple Python SSL Expiry Checker

A python script that prompts you for a domain name and checks if its SSL/TLS certificate is expired or expiring soon.

## How to Run

1. Open your terminal or command prompt.
2. Make sure you are in the folder where the script is saved.
3. Run the script using Python:
   ```bash
   python ssl_expiry_checker.py
   ```
4. Enter the domain you want to check when prompted (for example, `google.com` or `github.com`).

## How It Works

- **Input Prompt**: Asks you to type in a domain name. It automatically cleans the input if you copy-paste the whole URL (like `https://example.com/page`).
- **Connection**: It makes a secure connection to the website on port 443 (which is the default port for secure HTTPS websites).
- **Certificate Inspection**: It requests the SSL certificate from the server and looks at the `notAfter` date (which is when the certificate expires).
- **Time Calculation**: It calculates the difference between the expiry date and today's date in days.
- **Alert Status**:
  - If days left is less than 0, it tells you the certificate has **EXPIRED**.
  - If days left is 30 or less, it shows a **WARNING** that it is expiring soon.
  - Otherwise, it displays **OK**.
- **Error Handling**: If the website does not exist, has connection problems, or has an invalid SSL setup, the script prints out a clear error message instead of crashing.
