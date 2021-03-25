const getData = async() => {
	const url = "/candidate";
	const {data} = await axios.get(url);
	return data;
}

function ResultPage() {
	this.init = (resultList) => {
		this.resultList = [...resultList]
		this.setElements()
		this.bindEvents()
	}

	
	this.setElements = async() => {
		this.information = getData().then(function(resolvedData){
			console.log(resolvedData);
			console.log(resolvedData.user);
			return resolvedData;
		})


		console.log(this.information);

		this.template = /*html*/ `
			<div id="result-page">
				<div class="inner-container">
					<h1 class="title">Result 🥸</h1>
					<div class="result-container"></div>
					<div> Hello World! </div>
					<button class="restart-btn">RESTART</button>` +this.information +`
				</div>
      </div>
    `

		this.target = document.createElement('div')
		this.target.innerHTML = this.template
		this.target = this.target.firstElementChild

		this.resultContainer = this.target.querySelector('.result-container')
		this.restartBtn = this.target.querySelector('.restart-btn')
	}


	this.bindEvents = async() => {
		this.restartBtn.addEventListener('click', this.clickEventListener)
	}

	this.clickEventListener = async() => {
		router.route('quiz')
	}
}


