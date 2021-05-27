<template>
	<div>
		<img alt="Vue logo" src="../assets/logo.png" style="width: 200px"><span style="font-size: 120pt"> операции</span>
		<h1>Доброе утро</h1>
		<h1>Логические операции</h1>
		<ul>
			<li><b>=></b> импликация</li>
			<li><b>*</b> конъюнкция</li>
			<li><b>+</b> дизъюнкция</li>
			<li><b>!</b> отрицание</li>
			<li><b>()</b> скобки</li>
			<li><b>=</b> эквивалентность</li>
			<li><b>^</b> исключающее или (xor)</li>
		</ul>
	</div>
</template>

<script>
// @ is an alias to /src

export default {
	name: 'Docs'
}
</script>

<style scoped>
	h3 {
		margin: 40px 0 0;
	}
	ul {
		list-style-type: none;
		padding: 0;
	}
	li {
		display: inline-block;
		margin: 0 10px;
	}
	a {
		color: #42b983;
	}
	ul, ul li {
		display: block;
	}
</style>