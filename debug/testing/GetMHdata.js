/* Pull up the website in chrome
/ https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/depression-anxiety-self-assessment-quiz/
/ and run this script in the javasacript command line.
/ This is incomplete, make sure there's a way for it to
/ dump data over time to a file to prevent from having to
/ copy a multi million line object that crashes chrome */

(function(console){

console.save = function(data, filename){

    if(!data) {
        console.error('Console.save: No data')
        return;
    }

    if(!filename) filename = 'console.json'

    if(typeof data === "object"){
        data = JSON.stringify(data, undefined, 4)
    }

    var blob = new Blob([data], {type: 'text/json'}),
        e    = document.createEvent('MouseEvents'),
        a    = document.createElement('a')

    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
 }
})(console)

nums = []
data = {}
for (let i = 0; i < 1000000; i++) {
	nums.push(Math.floor(Math.random() * 4))
}

y = 0
for (let i = 0; i <= 1000000; i++){
frame = ""
document.getElementsByClassName("antbits-SA-std_btn")[0].click()

for (let x = 0; x <= 17; x++){
		y += 1
		if (y % 7) {
			y += 3
		}
		if (y >= 1000000) {
			y -= 1000000
		}
		p = nums[y]
		if (x == 8) {
			p = p % 2
		}
		frame += p.toString()
		await new Promise(r => setTimeout(r, 300))
		document.getElementById("antbits-SA-answer_"+x+"_"+p).click()
		await new Promise(r => setTimeout(r, 200))
		document.getElementById("antbits-SA-nav_next").click()
		if (i % 500 == 0 && i != 0) {
			console.save(data)
			data = {}
		}
}

await new Promise(r => setTimeout(r, 2000))
//data.push([frame, document.getElementsByClassName("antbits-SA-impact")[0].innerHTML, document.getElementsByClassName("antbits-SA-impact")[1].innerHTML])
data[frame] = [document.getElementsByClassName("antbits-SA-impact")[0].innerHTML, document.getElementsByClassName("antbits-SA-impact")[1].innerHTML]

//console.log(frame)
//console.log(document.getElementsByClassName("antbits-SA-impact")[0].innerHTML)
//console.log(document.getElementsByClassName("antbits-SA-impact")[1].innerHTML)

document.getElementById("antbits-SA-nav_links").click()
document.getElementById("antbits-SA-nav_finish").click()
await new Promise(r => setTimeout(r, 500))
}
console.save(data)