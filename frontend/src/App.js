import React, { useEffect } from 'react'
import './App.css'
import TarotCard from './components/TarotCard'

function App() {
	useEffect(() => {
		if (window.Telegram && window.Telegram.WebApp) {
			const telegram = window.Telegram.WebApp
			telegram.ready()
		} else {
			console.log('Telegram WebApp not found')
		}
	}, [])

	return (
		<div className='App'>
			<h1>Гадание на Таро</h1>
			<TarotCard />
		</div>
	)
}

export default App
