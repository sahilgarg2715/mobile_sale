from api.models import MSReceivedVouchers, MSOrderVouchers


ms_received_vouchers_qs = MSReceivedVouchers.objects.all()
for ms_received_voucher in ms_received_vouchers_qs:
    ms_voucher_qs = MSOrderVouchers.objects.filter(
        voucher_no=ms_received_voucher.voucher_no, pin=ms_received_voucher.pin
    )
    if ms_voucher_qs.exists():
        ms_voucher = ms_voucher_qs.first()
        if ms_voucher.amount < ms_received_voucher.amount:
            print(
                f"Voucher no: {ms_voucher.voucher_no} and Voucher Pin {ms_voucher.pin} with balance left { ms_received_voucher.amount - ms_voucher.amount} original amount: { ms_received_voucher.amount}  "
            )
