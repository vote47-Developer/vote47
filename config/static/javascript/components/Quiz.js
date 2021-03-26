function Quiz(parent, props) {
	this.init = () => {
		for (let key in props) {
			this[key] = props[key]
		}

		this.setElements()
		this.bindEvents()
	}
	// 문항별 배경지식이 보일 수 있게 
	this.backgrounds = 
    [0, 
        '이번 서울시장 선거는 재/보궐 선거로써, 원래의 4년 임기를 모두 수행하는 것이 아닌, <b>2022년 3월까지 약 1년간 임기를 수행</b>하게 됩니다. 그렇기 때문에 남은 임기를 수행할 때 후보자들의 정치 경험이 중요하다는 의견이 나오고 있어요.', 
        '후보자들의 성실성은 <b>국회 출석률</b>과 <b>법안 발의율</b>을 같은 시기 동료 의원들과 비교해서 상위 퍼센티지로 계산합니다.',
        '지방세법에 의하면, 시가표준액이 6억원 이하인 주택에 한정하여 재산세율 특례를 적용하고 있지만, 현재 서울지역의 아파트 중위값은 9억원입니다. 따라서 <b>재산세율을 높이면 지금보다 더 많은 사람들이 세금을 내게 되어서 서울시의 재정 여력이 늘어나게</b> 되고, <b>재산세율을 낮추면 세금을 내는 가계의 부담이 줄어들게</b> 됩니다.',
        '서울시에는 강남 한강변 부지에 <b>층고제한</b>이 걸려있습니다. 만약 이 층고제한을 해제하면 더 높은 아파트를 지을 수 있어 공급이 늘어날 수 있지만, 조망권 제한과 환경파괴등의 부작용이 일어날 수 있습니다. <b>용적률</b>이란 대지면적 대비 건물면적을 뜻하는데, 용적률이 높으면 같은 크기의 땅에 더 많은 건물을 지을 수 있어 공급이 늘어날 수 있지만, 적정 주거환경이 보장되지 않는 등 부작용이 일어날 수 있습니다. <b>공공부지</b>를 활용하면 기존의 공공임대 재건축으로 주택을 공급할 수 있지만, 집값에 대한 기대심리가 반영되지 못해 실효성이 떨어질 수 있습니다.',
        '광화문광장 재정비 사업은 지난 2020년 11월에 시작했습니다. 2021년 11월에 완공을 목표로 약 800억 원의 예산이 들어가는 이 사업은 광화문광장을 확장해서 공원과 같은 광장으로 만드는 것이 목표입니다. 하지만 이 사업을 두고 <b>공사중에 시민보행과 차량통행에 큰 불편을 초래하고 있다는 불만</b>과 <b>도심의 중심부에 녹색공원을 만들어 새로운 랜드마크로 삼아야 한다는 찬성</b>이 충돌하고 있습니다.',
        '사태가 터지고 LH와 SH등 공공기관에서는 소속 직원들을 대상으로 자체 전수조사를 진행했어요. 하지만 내부조사는 외부감사보다 조사의 정도나 수위가 낮아서 실효성이 없기 때문에 특검이나 검찰 주도의 수사가 필요하다는 지적이 있습니다. <b>특검은 특별검사제도</b>의 약자로, 한 달 정도의 수사 착수시간이 필요하고, 공정성이 필요한 사안에 진행하는 수사입니다. 이번 LH사태에서는 특검은 법적으로 경찰이 진행하게 되는데, 원칙대로 경찰의 수사권을 보장하자는 의견과 검찰에게 수사권을 줘서 수사를 진행하자는 의견이 있어요.',
        '코로나 사태로 어려운 상황에 재난지원금의 지급을 두고 <b>어려운 상황이니 지급해야 한다는 옹호의견</b>과, <b>현금살포성 포퓰리즘 공약이라는 비판</b>, 그리고 <b>오히려 코로나 특수를 누리는 사람들이 있기 때문에 선별 지급해야 한다는 의견</b>이 맞서고 있어요.',
        '박원순 전 시장의 성추문으로 인해 치뤄지게 된 이번 선거는 어느때보다도 여성의 안전과 밀접하게 관련이 되어 있습니다. 후보자들도 여성의 안전을 보장하기 위해 여러 공약을 제시했는데, 실효성이 없는 정책이라는 비판의견도 있습니다. 이 중 어떤 방법이 가장 효과적일까요?',
        '대한민국은 2020년 기준 UN에 등록된 나라중 출산율이 가장 낮았습니다. 심지어 OECD국가중에는 유일하게 1을 밑도는 0.84를 기록했는데요, 이대로라면 2060년에는 65세 이상의 노인이 전체 인구의 41.6퍼센트가 될 것이고, 2100년에는 한국 인구가 2500만 명으로 반토막이 나게 된다는 예측도 있습니다. 따라서 이런 문제를 해결하기 위해서 서울시 차원의 대책이 필요하다는 목소리가 나오고 있습니다.',
        '급변하는 사회에 맞춰서 학생들에게 필요한 교육도 변하고 있어요. 서울시장 선거에서도 학생들의 교육과 관련된 공약이 많은 관심을 얻고 있어요. 미래산업의 중심이 될 서울시의 학생들에게 어떤 교육정책이 도움이 될까요?',
        '경제 불황과 코로나 사태로 인해서 청년들의 실업 문제가 심각해지고 있습니다. 청년들의 실업과 일자리 문제는 장기적으로 부동산과 출산율의 문제로도 이어지곤 합니다. 몇 년째 여러 정책으로도 나아지지 않고 있는 실업 문제, 어떤 정책이 취업준비생들에게 가장 필요할까요?',
        '코로나 사태로 많은 자영업자들이 힘들어하고 있어요. 서울 시민 4명중 1명이 자영업자라는 통계도 있을 만큼 주변에 많은 소상공인들이 있는데, 이분들을 도와주기 위해서 양 후보는 현금 지원성 정책을 들고 왔습니다. 다음 중 어떤 공약의 지원의 범위와 규모가 적합할까요?',
        '다양성에 대한 가치가 점점 중요해지면서 퀴어축제와 관련된 논란이 생기고 있어요. <b>성소수자를 포함한 모든 사람은 자신의 의견을 자유롭게 표출할 권리가 있기 때문에 서울 중심부에서 퀴어축제를 진행해야한다는 의견</b>과 <b>과도한 노출과 선정성 논란이 있는 퀴어축제를 어린아이들이 볼 수도 있는 곳에서 여는 것은 바람직하지 않다는 의견</b>이 마찰을 만들고 있어요.',
        '서울시 장애인의 비율은 전체 인구의 약 6%에 이릅니다. 장애인과 비장애인의 동반성장의 가치를 위해서 이미 여러 정책들이 시행되고 있지만, 아직도 장애인들의 생활은 불편함이 많습니다. 다음 정책들 중에서 어떤 공약이 장애인들을 위한 정책으로 중요할까요?',
        '이번 테스트에서는 후보자들의 공약을 크게 5개의 카테고리와 후보자 개인의 질문으로 나눠서 제작했습니다. 다음 6가지 선택지중, 유권자님이 가장 중요하다고 생각하는 선택지는 무엇인가요?',
    ]
	this.setElements = () => {
		this.template = /*html*/ `
		<div class="quiz dp-none" data-id="${this.id}">
		    <div class="question">
		    	<div class="question__content">
		    		Q${this.id}. ${this.question}	
		    	</div>
                <br>
		    	<button class="open"> 질문에 대한 배경 설명 🤔 </button>
		    	<div class="modal-wrapper" style="display: none;">
		    	<div class="modal">
		    		<div class="modal-title"></div>
		    		<p>${this.backgrounds[this.id]}</p>
		    		<div class="close-wrapper" >
		    			<button class="close">닫기</button>
		    		</div>
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
			answerIndex: +exampleElem.dataset.index+1,
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