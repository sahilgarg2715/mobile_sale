from openpyxl import load_workbook
from api.models import MSReceivedVouchers

wb = load_workbook("voucher_info.xlsx")
for ws in wb.worksheets:
    for i in range(1, ws.max_row + 1):
        voucher_no = ws.cell(column=1, row=i).value
        pin = str(ws.cell(column=2, row=i).value)
        amount = ws.cell(column=3, row=i).value
        if voucher_no is not None and pin is not None:
            pin = pin.replace("'", "")
            ms_voucher_info, created = MSReceivedVouchers.objects.get_or_create(
                voucher_no=voucher_no, pin=pin, amount=amount
            )

print("done processing")
