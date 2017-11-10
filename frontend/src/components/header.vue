<template>
    <header class="header inner">
		<div class="alignleft">
			<h1>
				<a href="">Light</a>
			</h1>
		</div>
		<nav class="alignright main-nav">
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="#">Archives</a></li>
				<li><a href="#">Pages</a></li>
			</ul>
		</nav>
		<div class="clearfix"></div>
	</header>
</template>
<script>
export default{
    
}
</script>
<style scoped>
.header {
    text-shadow: 0 0 1px #fff;
    margin: 50px auto;
	color: #999;
}

.header h1 a{
	font-size: 35px;
	color: #999;
}
.header .main-nav li{
	float: left;	
    margin-left: 30px;
}
.alignleft {
    float: left;
}
.alignright {
    float: right;
}
</style>

