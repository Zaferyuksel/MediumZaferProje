const container = document.getElementById("karbox");
		const letters = "M";

		function createLetter() {
			const letter = document.createElement("span");
			letter.className = "letter";
			letter.innerText = letters[Math.floor(Math.random() * letters.length)];
			letter.style.left = Math.random() * 100 + "%";
			container.appendChild(letter);
			setTimeout(() => letter.remove(), 5000);
		}

		setInterval(createLetter, 100);