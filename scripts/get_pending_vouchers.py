from api.models import MSReceivedVouchers, MSOrderVouchers


ms_received_vouchers_qs = MSReceivedVouchers.objects.all()
pending_bal = 0
for ms_received_voucher in ms_received_vouchers_qs:
    ms_voucher_qs = MSOrderVouchers.objects.filter(
        voucher_no=ms_received_voucher.voucher_no, pin=ms_received_voucher.pin
    )
    if ms_voucher_qs.exists():
        ms_voucher = ms_voucher_qs.first()
        diff = ms_received_voucher.amount - ms_voucher.amount
        if diff > 0:
            print(
                f"Voucher no: {ms_voucher.voucher_no} and Voucher Pin {ms_voucher.pin} with balance left: {diff} original amount: { ms_received_voucher.amount}  "
            )
            pending_bal = pending_bal + diff
    else:
        print(
            f"Unused voucher: Voucher no: {ms_received_voucher.voucher_no} and Voucher Pin {ms_received_voucher.pin} amount: { ms_received_voucher.amount}  "
        )
        pending_bal = pending_bal + ms_received_voucher.amount

print(pending_bal)
