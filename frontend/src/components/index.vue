<template>
    <section class="inner">
        <div class="main-col alignleft">
            <div class="wrap">
                <article class="post">
                    <div class="post-content">
                        <header>
                            <div class="time">
                                Dec 29, 2015
                            </div>
                            <h1 class="title"> 
                                <a href="#">intro</a>
                            </h1>
                        </header>
                        <div class="entry markdown">
                            <p>文章文章。post-content</p>
                        </div>
                    </div>
                </article>
                <article class="post">
                    <div class="post-content">
                        文章文章。post-content
                    </div> 
                </article>
            </div>
        </div>
        <aside class="siderbar alignright">
            <div class="search">
                <input type="text" name="search" placeholder="search">
            </div>
            <div class="widget tag">
                <h3 class="title">
                    Tags
                </h3>
                <ul class="entry">
                    <li><a href="#">Javascript</a><small>2</small></li>
                    <li><a href="#">Python</a><small>6</small></li>
                    <li><a href="#">Life</a><small>4</small></li>
                </ul>
            </div>
            <div class="widget twitter">
                <h3 class="title">Tweets</h3>
            </div>
        </aside>
    </section>  
</template>
<script>
export default{
    
}
</script>
<style>
.main-col{
    width: 900px; 
}
.post{
    box-shadow: 1px 2px 3px #ddd;
    background: #fff;
}
.post-content{
    padding: 20px 20px 15px 77px;
    margin-bottom: 50px;
    position: relative;
    height: 200px;
}
.siderbar{
    width: 270px;
    line-height: 1.8em;
}
.search{
    margin-bottom: 30px;
}
.siderbar .search input{
    background: #fff;
    font-family: "Lato", Helvetica Neue, Helvetica, Arial, sans-serif;
    font-style: italic;
    font-size: 1em;
    padding: 10px 15px;
    border: 1px solid #ddd;
    width: 100%;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    color: #999;
}
.widget {
    background: #fff;
    box-shadow: 1px 2px 3px #ddd;
    margin-bottom: 30px;
}
.widget .title{
    padding: 15px 20px;
    font-size: 1em;
    border-bottom: 1px solid #ddd;
    font-weight: normal;
}
.widget .entry{
    font-size: 0.9em;
    padding: 15px 20px;
}
.tag small{
    margin-left: 15px;
    color: #999;
}
.tag small:before {
  content: '(';
}
.tag small:after {
  content: ')';
}
.post-content .title a {
    font-size: 1.8em;
    color: #444;
}
.post-content .title a:hover{
    color: #258fb8;
}
.post-content .time{
    color: #258fb8;
}

</style>
