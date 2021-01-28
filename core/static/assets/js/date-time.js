(function($) {
    $(function() {
        $('#id_0').datetimepicker({
            useCurrent: false,
            "allowInputToggle": true,
            "showClose": true,
            "showClear": true,
            "showTodayButton": true,
            "format": "MM/DD/YYYY hh:mm:ss A",
        });

        $('#id_1').datetimepicker({
            useCurrent: false,
            "allowInputToggle": true,
            "showClose": true,
            "showClear": true,
            "showTodayButton": true,
            "format": "MM/DD/YYYY hh:mm:ss A",
        });

        $("#id_0").on("dp.change", function(e) {
            $('#id_1').data("DateTimePicker").minDate(e.date);

        });
        $("#id_1").on("dp.change", function(e) {
            $('#id_0').data("DateTimePicker").maxDate(e.date);

        });

    });
})(jQuery);