import React, { useState } from 'react'
import tarotCards from '../data/tarotCards'

function TarotCard() {
	const [card, setCard] = useState(null)

	const drawCard = () => {
		const randomCard = tarotCards[Math.floor(Math.random() * tarotCards.length)]
		setCard(randomCard)
	}

	return (
		<div>
			{card ? (
				<div>
					<h2>{card.name}</h2>
					<p>{card.description}</p>
				</div>
			) : (
				<p>Нажми на кнопку, чтобы вытянуть карту.</p>
			)}
			<button onClick={drawCard}>Вытянуть карту</button>
		</div>
	)
}

export default TarotCard
