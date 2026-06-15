1. Sơ đồ cấu trúc cây thư mục
   rikkei_aviation/
   │
   ├── core/
   │ ├── **init**.py
   │ ├── logistics.py
   │ └── manager.py
   │
   ├── utils/
   │ ├── **init**.py
   │ ├── file_helper.py
   │ └── time_helper.py
   │
   ├── main.py

2. Nên hạn chế dùng from math import \* vì có thể gây xung đột tên hàm, giảm tính tường minh, lãng phí bộ nhớ và giảm hiệu năng.
