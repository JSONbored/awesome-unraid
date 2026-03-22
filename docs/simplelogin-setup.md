# SimpleLogin Setup on Unraid
1. Install PostgreSQL and Redis (e.g. `postgres-shared` and `redis-shared`).
2. Install `SimpleLogin-Postfix`. Note: Port 25 must be forwarded from your router to Unraid.
3. Install `SimpleLogin-AIO`. Connect it to the DB and set the Postfix server IP.
4. Check the logs on first boot to grab the auto-generated DKIM DNS record.
5. Create DNS records:
   - `A mail.yourdomain.com -> YOUR_IP`
   - `MX yourdomain.com -> 10 mail.yourdomain.com`
   - `TXT yourdomain.com -> v=spf1 mx ~all`
   - `TXT _dmarc.yourdomain.com -> v=DMARC1; p=quarantine; rua=mailto:admin@yourdomain.com`
   - `TXT dkim._domainkey.yourdomain.com -> (from logs)`
