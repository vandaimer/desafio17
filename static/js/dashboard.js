DashboardModule = {
    onLoad : function() {
        $('.more-info').on('click', DashboardModule.populateModal);
    },

    populateModal : function() {

    }
};

$(document).ready(DashboardModule.onLoad);
