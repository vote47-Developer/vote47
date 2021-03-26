function StartPage() {
	this.init = () => {
		this.setElements()
		this.bindEvents()
	}

	this.setElements = () => {
		this.template = /*html*/ `
      <div id="start-page">
        <h1 class="title"><i class="fas fa-vote-yea" style='color:#9956f6'></i> Welcome To Vote47</h1>
        <div class='info'>
            <p><i class="fas fa-exclamation"></i>  테스트는 총 15문제이고, 약 7분가량 걸려요.</p>
            <p><i class="fas fa-exclamation"></i>  3월 19일 후보자 등록기간 중 여론조사에서 <br> 10%이상의 지지도를 기록한 후보들이 대상이에요.</p>
            <p><i class="fas fa-exclamation"></i>  지지 정당이나 이념, 후보에 대한 선호도는 반영되지 않아요.</p>
            <p><i class="fas fa-exclamation"></i>  내 생각과 후보의 공약의 일치율만 결과에 표시돼요.</p>
            <p><i class="fas fa-exclamation"></i>  이 결과는 예상 일치도이며, 선택은 유권자님의 몫이에요.</p>
        </div>
        <button class="start-btn">테스트 시작</button>
      </div>
    `
		this.target = document.createElement('div')
		this.target.innerHTML = this.template
		this.target = this.target.firstElementChild

		this.startBtn = this.target.querySelector('.start-btn')
	}

	this.bindEvents = () => {
		this.startBtn.addEventListener('click', this.clickEventListener)
	}

	this.clickEventListener = () => {
		router.route('quiz')
	}
}
