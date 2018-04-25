<template>
    <section class="inner">
        <div class="main-col alignleft">
            <div class="wrap">
                <article class="post">
                    <div class="post-content">
                        <header>
                            <h1 class="title post-title">
                                <span>{{post.title}}</span>
                            </h1>
                            <div class="time">
                                日期：{{post.created_time | limitTo(10)}}
                            </div>
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

export default{

    created(){
        this.getPost(this.$route.params.id);
    },
    data(){
        return {
            post:{}
        }
    },
    components:{
        tags,
        categories,
    },
    methods:{
        //获取所有post 数据
        getPost(id){
            this.$http.get('api/post/' + id)
            .then(res => {
                this.post = res.data;
                this.post.body = Marked(this.post.body)
                console.log(res.data)
            })
        }
    }
}
</script>
<style scoped>
.post-title{
    text-align: center;
    margin-bottom: 20px;
}
</style>
