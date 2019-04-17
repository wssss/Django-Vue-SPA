<template>
    <header class="header inner">
		<div class="alignleft">
			<h1>
				<a href="">我是豆豆g__</a>
			</h1>
		</div>
		<nav class="alignright main-nav">
			<ul>
				<li><router-link to="/">Home</router-link></li>
				<li><router-link to="archives">archives</router-link></li>
				<li><a href="#">Pages</a></li>
				<li><router-link to="tushare">tushare</router-link></li>
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
}

.header h1 a{
	font-size: 2.5em;
}
.header a {
	color: #999;
}

.header a:hover{
	color: #258fb8;
}
.main-nav{
	line-height: 2.5em;
}
.header .main-nav li{
	float: left;	
    margin-left: 30px;
}
</style>

