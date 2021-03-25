function Quiz(parent, props) {
	this.init = () => {
		for (let key in props) {
			this[key] = props[key]
		}

		this.setElements()
		this.bindEvents()
	}

	this.setElements = () => {
		this.template = /*html*/ `
		<div class="quiz dp-none" data-id="${this.id}">
		<div class="question">Q. ${this.question}</div>
		<button class="open">모달열기</button>
		<div class="modal-wrapper" style="display: none;">
			<div class="modal">
				<div class="modal-title">모달 제목</div>
				<p>모달 내용은 이렇습니다!</p>
				<div class="close-wrapper" >
					<button class="close">닫기</button>
				</div>
			</div>
    	</div>
        <ul class="example-container">
          ${this.examples
						.map(
							(example, index) =>
								/*html*/ `<li class="example" data-index="${index}">${example.title}</li>`
						)
						.join('')}
        </ul>
      </div>
    `
		
		this.target = document.createElement('div')
		this.target.innerHTML = this.template
		this.target = this.target.firstElementChild

		this.exampleContainer = this.target.querySelector('.example-container')
		this.open = this.target.querySelector('.open');		
		this.close = this.target.querySelector('.close');		
	}

	this.bindEvents = () => {
		this.open.addEventListener('click', (e) => {
			e.target.nextElementSibling.style.display = 'flex';
		})
		this.close.addEventListener('click', (e) => {		
			e.target.parentNode.parentNode.parentNode.style.display = 'none';
		})
		this.exampleContainer.addEventListener('click', (e) => {
			this.clickEventListener(e)
		})
	}

	this.clickEventListener = (e) => {
		const closestExampleElem = e.target.closest('.example')
		
		if (closestExampleElem) {
			this.selectAnswer(e, closestExampleElem)
		}
	}

	this.selectAnswer = (e, exampleElem) => {
		const unselectedExamples = this.target.querySelectorAll(
			`.example:not([data-index="${exampleElem.dataset.index}"])`
		)
		unselectedExamples.forEach((example) => {
			example.style.transform = `translateY(16px) scale(0.75)`
			example.style.opacity = 0
		})
		exampleElem.classList.add('active')
		this.saveAnswer(exampleElem)
		parent.selectAnswer({
			quizId: this.id,
			answerIndex: +exampleElem.dataset.index,
		})
	}
	// 추가한 코드
	//todo 문항번호 같이 넘기기
	this.saveAnswer = (exampleElem) => {
		let exampleId = +exampleElem.dataset.index+1;
		let url = 'answer';
		axios.post(url, {
			quizId: this.id,
			exampleId: exampleId,
		})
				.then(
					(response) => {
					}
				)
	}

	this.hide = () => {
		this.target.classList.add('dp-none')
	}

	this.show = () => {
		this.target.classList.remove('dp-none')
		this.target.style.opacity = 0
		setTimeout(() => {
			this.target.style.opacity = 1
		}, 0)
	}
	this.init()
} 

