
var colours = ['#ff453a', '#ff453a', '#fa493a', '#f44c3b', '#ef503b', '#ea543c', '#e5583c', '#df5b3d', '#da5f3d', '#d5633d', '#d0673e', '#ca6a3e', '#c56e3f', '#c0723f', '#bb7640', '#b57940', '#b07d41', '#ab8141', '#a68541', '#a08842', '#9b8c42', '#969043', '#919443', '#8b9744', '#869b44', '#819f44', '#7ca345', '#76a645', '#71aa46', '#6cae46', '#67b247', '#61b547', '#5cb948', '#57bd48', '#52c148', '#4cc449', '#47c849', '#42cc4a', '#3dd04a', '#37d34b', '#32d74b', '#32d74b']

// Update the page with a new random number every second
function jsfunction() {



    setInterval(function () {
        $.getJSON('/api', function (data) {


            // Convert the fajr prayer time to a Date object
            var fajr = new Date();
            var fajrTime = data.fajr.split(':');
            fajr.setHours(fajrTime[0]);
            fajr.setMinutes(fajrTime[1]);
            fajr.setSeconds(0);

            // Convert the zuhr prayer time to a Date object
            var zuhr = new Date();
            var zuhrTime = data.zuhr.split(':');
            zuhr.setHours(zuhrTime[0]);
            zuhr.setMinutes(zuhrTime[1]);
            zuhr.setSeconds(0);

            // Convert the asr prayer time to a Date object
            var asr = new Date();
            var asrTime = data.asr.split(':');
            asr.setHours(asrTime[0]);
            asr.setMinutes(asrTime[1]);
            asr.setSeconds(0);

            // Convert the maghrib prayer time to a Date object
            var maghrib = new Date();
            var maghribTime = data.maghrib.split(':');
            maghrib.setHours(maghribTime[0]);
            maghrib.setMinutes(maghribTime[1]);
            maghrib.setSeconds(0);

            // Convert the isya prayer time to a Date object
            var isya = new Date();
            var isyaTime = data.isya.split(':');
            isya.setHours(isyaTime[0]);
            isya.setMinutes(isyaTime[1]);
            isya.setSeconds(0);

            // Get the current time
            var now = new Date();
            var now_hours = now.getHours().toString().padStart(2, '0');
            var now_minutes = now.getMinutes().toString().padStart(2, '0');

            // Concatenate the hours and minutes into a single string in the format "hh:mm"
            var nowString = now_hours + ':' + now_minutes;

            // Create an array with the prayer times and the current time
            var times = [fajr, zuhr, asr, maghrib, isya];

            // Sort the array of times based on their value
            times.sort(function (a, b) {
                return a - b;
            });

            // Find the nearest prayer time
            var nearestTime = times[0];
            for (var i = 0; i < times.length - 1; i++) {
                if (times[i] > now) {
                    nearestTime = times[i];
                    break;
                }
            }

            // Calculate the elapsed time
            var elapsedTime = nearestTime - now;

            if (elapsedTime < 0) {
                elapsedTime += 1000 * 60 * 60 * 24;
            }

            // Convert the elapsed time to hours, minutes, and seconds
            var hours = Math.floor(elapsedTime / (1000 * 60 * 60));
            var minutes = Math.floor((elapsedTime % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((elapsedTime % (1000 * 60)) / 1000);

            // Convert the hours, minutes, and seconds to strings and add leading zeros if necessary
            hours = hours.toString().padStart(2, '0');
            minutes = minutes.toString().padStart(2, '0');
            seconds = seconds.toString().padStart(2, '0');

            // Concatenate the hours, minutes, and seconds into a single string in the format "hh:mm:ss"
            var elapsedTimeString = hours + ' : ' + minutes + ' : ' + seconds;

            // Update the clock element with the elapsed time
            $('#clock').html(elapsedTimeString);
            $('#time').html(nowString);
            $('#time-fajr').html(data.fajr)
            $('#date-upper').html(data.date)
            $('#hijri-date').html(data.hijri)
            $('#time-zuhr').html(data.zuhr)
            $('#time-asr').html(data.asr)
            $('#time-maghrib').html(data.maghrib)
            $('#time-isya').html(data.isya)

            $('#total_vacancy').html(data.num);
            // Update the fill color of the SVG

            $('.mint-round-red').css('background-image', 'url(../static/assets/images/mint-round/'+data.num+'.svg)');


        });




    }, 1000);


}






const element = document.querySelector('.mint-prayer h1');

function updateElement() {
    // Update the text of the element
    // element.textContent = 'New text';

    // Reset the animation by removing and re-adding the animation class
    element.classList.remove('fadeIn');
    void element.offsetWidth; // trigger reflow
    element.classList.add('fadeIn');
}

setInterval(updateElement, 3000); // update the element every 3 seconds