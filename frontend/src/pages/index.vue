<template>
    <section class="inner">
        <div class="main-col alignleft">
            <div class="wrap">
                <article class="post" v-for="post in posts">
                    <div class="post-content">
                        <header>
                            <div class="time">
                                日期：{{post.created_time | limitTo(10)}}
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
    },
    filters:{
        limitTo:function(str, len){
            return str.substr(0, len)
        }
    }
}
</script>
<style>



</style>
