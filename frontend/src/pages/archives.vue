<template>
    <section class="inner">
         <div class="main-col alignleft">
             <div class="wrap">
                 <article class="post" v-for="post in posts" :key="post.id">
                     <div class="list-content">
                         <header>
                             <div class="item">
                                 日期：{{post.created_time | limitTo(10)}}
                             </div>
                             <h1 class="title">
                                  <router-link :to="{ name: 'post', params:  { 'id': post.id}}">{{post.title}}</router-link>
                              </h1>
                         </header>
                         <div class="excerpt">
                             {{ post.excerpt }}
                         </div>
                     </div>
                 </article>
             </div>
         </div>
         <aside class="siderbar alignright">
              <search></search>
              <categories></categories>
              <tags></tags>
        </aside>
    </section>
</template>
<script>
import tags from '@/components/tags';
import categories from '@/components/categories';
import search from '@/components/search'

export default {
    created(){
        this.getPosts()
    },
    data(){
        return {
            posts:[]
        }
    },
    components:{
        tags,
        categories,
        search
    },
    methods:{
        getPosts(){
            this.$http.get('api/post/')
            .then(res => {
                this.posts = res.data.results;
                //this.post.body = Marked(this.post.body)
                console.log(res.data)
            })
        }
    }
}

</script>
<style scoped>
.list-content{
    padding: 20px 20px 15px 20px;
    margin-bottom: 20px;
    position: relative;
    min-height: 40px;
}
.list-content .title a{
    font-size:1.6em
}
.list-content .excerpt{
    padding: 20px 0 0;
}
</style>
