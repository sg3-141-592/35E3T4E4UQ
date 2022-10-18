This is a helper service to re-direct your naked domain (e.g. mysite.com) to an appropriate CNAME record.

I developed this to get around redirecting my GoDaddy site dishy.dev to www.dishy.dev.

## Nginx
``` bash
nginx -s reload
docker exec -it nginx-server nginx -s reload
docker logs -f nginx-web-1 1>/dev/null # error.log
docker logs -f nginx-web-1 2>/dev/null # access.log
```

## Process
- Check if URL already points somewhere
- User adds A-Record
- Generate certificate using http challenge
- Validate certificate
- Done