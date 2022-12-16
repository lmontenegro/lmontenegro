def totalCart(request):
    total = 0
    total_item = 0
    if "cart" in request.session.keys():
    	for key, value in request.session["cart"].items():
            total += int(value["accumulated"])
            total_item += int(value["cantity"])
    return {"total_cart": total, "cantity": total_item}

