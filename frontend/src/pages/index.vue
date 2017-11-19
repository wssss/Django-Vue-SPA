<template>
    <section class="inner">
        <div class="main-col alignleft">
            <div class="wrap">
                <article class="post" v-for="post in posts">
                    <div class="post-content">
                        <header>
                            <div class="time">
                                {{post.created_time}}
                            </div>
                            <h1 class="title"> 
                                <router-link :to="{ name: 'post', params:  { 'id': post.id}}">{{post.title}}</router-link>
                            </h1>
                        </header>
                        <div class="entry markdown">
                            <div v-highlight v-html="post.body"></div>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        <aside class="siderbar alignright">
            <div class="search">
                <input type="text" name="search" placeholder="search">
            </div>   
            <categories></categories>
            <tags></tags> 
        </aside>
    </section>  
</template>
<script>
import Marked from 'marked';
import tags from '@/components/tags';
import categories from '@/components/categories'
import 'highlight.js/styles/monokai-sublime.css'

export default{

    created(){
        this.getPosts();
    },
    data(){
        return {
            posts:[]
        }
    },
    components:{
        tags,
        categories,
    },
    methods:{
        //获取所有post 数据
        getPosts(){
            this.$http.get('api/post')
            .then(res => {
                this.posts = res.data;
                for(let i=0; i < this.posts.length; i++){
                    this.posts[i].body = Marked(this.posts[i].body)
                }
                console.log(res.data)
            })
        }
    }
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
    min-height: 200px;
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
.widget small{
    margin-left: 15px;
    color: #999;
}
.widget small:before {
  content: '(';
}
.widget small:after {
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
