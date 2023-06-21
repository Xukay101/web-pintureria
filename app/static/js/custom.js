function decrementQuantity(productId) {
    var input = document.querySelector('input[name="quantity_' + productId + '"]');
    var currentValue = parseInt(input.value);
    if (currentValue > 1) {
        input.value = currentValue - 1;
    }
}

function incrementQuantity(productId) {
    var input = document.querySelector('input[name="quantity_' + productId + '"]');
    var currentValue = parseInt(input.value);
    input.value = currentValue + 1;
}
