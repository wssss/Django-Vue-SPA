<template>
    <section class="inner">
        <div class="main-col alignleft">
            <div class="wrap">
                <article class="post" v-for="post in posts" :key="post.id">
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
                            <div class="read-more">
                                <router-link :to="{ name: 'post', params:  { 'id': post.id}}">阅读全文</router-link>
                            </div>
                        </div>
                    </div>
                </article>
            </div>
            <pagination :total="page_state.total" :size="page_state.page_size" :page="page_state.page_num" :change="pageChange" :isUrl="false"></pagination>
        </div>
        <aside class="siderbar alignright">
            <search></search>  
            <categories></categories>
            <tags></tags>
        </aside>
        <div class="clearfix"></div>
    </section>
</template>
<script>
import Marked from 'marked';
import tags from '@/components/tags';
import categories from '@/components/categories'
import search from '@/components/search'
import pagination from '@/components/pagination'
import 'highlight.js/styles/monokai-sublime.css'


export default{
    data(){
        return {
            posts:[],
            page_state:{
                page_size:3,
                page_num:this.$route.query.page_num || 1,
                total:10
            }
        }
    },
    components:{
        tags,
        categories,
        search,
        pagination
    },
    methods:{
        //获取所有post 数据
        getPosts(){
            this.$http.get('api/post?page_size=' + this.page_state.page_size + '&page_num=' + this.page_state.page_num)
            .then(res => {
                this.page_state.total = res.data.count;

                this.posts = res.data.results;
                for(let i=0; i < this.posts.length; i++){
                    this.posts[i].body = Marked(this.posts[i].body.substr(0, 300) + "...")
                }
                console.log(res.data)
            })
        },
        pageChange(val){ 
            this.page_state.page_num = val;
            this.$router.push({ query: {page_num: val }})
            this.getPosts()
        }
    }
}
</script>
<style scoped> 

.read-more{
    border: 1px solid #de686d;
    height: 32px;
    line-height: 32px;
    text-align: center;
    padding: 0 20px;
    margin: 40px auto 10px;
    font-size: 16px;
    color: #de686d;
    background: #fff;
    border-radius: 4px;
    border: 1px solid #de686d;
    line-height: 30px;
    width: 100px;
    cursor: pointer;
}
.read-more a{
    color: #de686d;
}

</style>
