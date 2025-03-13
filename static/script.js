$(document).ready(function(){

    $("#energy-form button").on("click", function(event){
        event.preventDefault();

        let energyData = {
            day_of_week: $("input[placeholder='Enter Day (0-6)']").val(),
            month: $("input[placeholder='Enter Month (1-12)']").val(),
            hour: $("input[placeholder='Enter Hour (0-23)']").val(),
            weekend: $("input[name='weekend']:checked").val() === "yes" ? 1 : 0,
            holiday: $("input[name='holiday']:checked").val() === "yes" ? 1 : 0,
            temperature: $("input[placeholder='Enter Temperature']").val(),
            humidity: $("input[placeholder='Enter Humidity']").val(),
            wind_speed: $("input[placeholder='Enter Wind Speed']").val(),
            solar_radiation: $("input[placeholder='Enter Solar Radiation']").val(),
            building_size: $("input[placeholder='Enter Building Size']").val(),
            occupants: $("input[placeholder='Enter Number of Occupants']").val(),
            building_type: $("input[placeholder='Enter Building Type']").val(),
            hvac_usage: $("input[placeholder='Enter HVAC Usage']").val(),
            lighting_usage: $("input[placeholder='Enter Lighting Usage']").val(),
            appliance_load: $("input[placeholder='Enter Appliance Load']").val(),
            prev_hour: $("input[placeholder='Enter Previous Hour Consumption']").val(),
            prev_day: $("input[placeholder='Enter Previous Day Consumption']").val(),
            prev_week: $("input[placeholder='Enter Previous Week Consumption']").val()
        };

        $.ajax({
            url: "/predict/energy",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(energyData),
            success: function(response){
                if(response.error) {
                    alert("Error: " + response.error);
                } else {
                    alert("Predicted Energy Consumption: " + response.prediction + " kWh");
                }
            }
        });
    });

    
    $("#water-form button").on("click", function(event){
        event.preventDefault();

        let waterData = {
            day_of_week: $("input[placeholder='Enter Day (0-6)']").val(),
            month: $("input[placeholder='Enter Month (1-12)']").val(),
            temperature: $("input[placeholder='Enter Temperature']").val(),
            rainfall: $("input[placeholder='Enter Rainfall']").val(),
            holiday: $("input[name='holiday']:checked").val() === "yes" ? 1 : 0,
            prev_day_water: $("input[placeholder='Enter Previous Consumption']").val(),
            building_size: $("input[placeholder='Enter Building Size']").val(),
            household_members: $("input[placeholder='Enter Number of Members']").val()
        };

        $.ajax({
            url: "/predict/water",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(waterData),
            success: function(response){
                if(response.error) {
                    alert("Error: " + response.error);
                } else {
                    alert("Predicted Water Consumption: " + response.prediction + " liters");
                }
            }
        });
    });

});
