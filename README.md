這是個測試

## 控制 Kawasaki 手臂範例

`kawasaki_move.py` 示範如何透過 TCP/IP 連線將關節角度設定為:

- jt1: 0
- jt2: 0
- jt3: 90
- jt4: 0
- jt5: -90
- jt6: 0

請依據實際控制器 IP 與 Port 修改 `HOST` 與 `PORT`，執行:

```bash
python3 kawasaki_move.py
```
