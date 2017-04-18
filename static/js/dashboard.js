DashboardModule = {
    onLoad : function() {
        $('.more-info').on('click', DashboardModule.populateModal);
    },

    populateModal : function() {
        var row = $(this).parents('.new-user');
        var name = $(row).find('.name').text();
        var amount = $(row).find('.amount').text();
        var phone = $(row).find('.phone').val();
        var order = $(row).find('.order').text();
        order = order.split(', ');
        var modal = $('#moreInfoModal');
        $(modal).find('#nameModal').text(name);
        $(modal).find('#amountModal').text(amount);
        $(modal).find('#phoneModal').text(phone);
        $(modal).find('#listOrderModal').empty();
        order.forEach(function(item, index) {
            $(modal).find('#listOrderModal').append('<li>'+item+'</li>');
        });
    },
}

$(document).ready(DashboardModule.onLoad);
