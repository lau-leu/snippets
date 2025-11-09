# Monter un partage CIFS

```bash
sudo mount -t cifs '//<ip>/<folder>' /<mount> -o vers=<smb_version>,user=<user>,rw,uid=userlocal,gid=userlocal
```

**Description** : Monte un partage CIFS avec les options spécifiées.
**Tags** : linux,mount,cifs,share
