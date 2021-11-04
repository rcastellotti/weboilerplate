
# init db

```
docker exec -it signs-rcastellotti-dev-backend python3 -c "from app import db; db.create_all()"
```