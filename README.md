# chromadb example

```bash
$ docker run -d --rm --name chromadb -p 8000:8000 -v ./chroma_db_path:/chroma/chroma -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE chromadb/chroma:latest
```

### collection create

```bash
$ python3 collection-create.py
```

### collection peek

all search on collection

```bash
$ python3 collection-peek.py
```

### collection add document

```bash
$ python3 collection-add.py
```

### collection query

similarity document search

```bash
$ python3 collection-query.py
```

### collection delete

```bash
$ python3 collection-delete.py
```