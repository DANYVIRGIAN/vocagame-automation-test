# VocaGame Automation Test

Repository ini berisi script automation testing untuk website VocaGame menggunakan **Python**, **Selenium**, dan **Pytest**.

## (Prerequisites)

Pastikan di komputer Anda sudah terinstall:
* Python 3.x

## Cara Install (Installation)

1.  **Buka Terminal** di folder project ini.
2.  **Buat Virtual Environment** (Opsional tapi disarankan):
    ```bash
    python -m venv venv
    ```
3.  **Aktifkan Virtual Environment**:
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate
        ```
    * **Windows (CMD):**
        ```cmd
        venv\Scripts\activate
        ```
    * **Mac/Linux:**
        ```bash
        source venv/bin/activate
        ```
4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Catatan: Jika file requirements.txt belum ada, install manual: `pip install selenium pytest webdriver-manager`)*

---

## Cara Menjalankan Test (How to Run)

### 1. Menjalankan SEMUA Test (Recommended)
Untuk menjalankan seluruh skenario (Register, Login, Order, Forgot Password) secara berurutan:
```bash
python -m pytest tests/ -v -s