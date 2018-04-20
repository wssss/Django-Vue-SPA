<template>
    <section class="inner">
         <div class="main-col alignleft">
             <div class="wrap">
                 <article class="post" v-for="post in posts">
                     <div class="list-content">
                         <header>
                             <div class="item">
                                 {{ post.created_time }}
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
import categories from '@/components/categories';

export default {
    created(){
        this.getPosts(this.$route.query.category|| '', this.$route.query.tag||'')
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
        getPosts(category, tag){
              this.$http.get('api/post/?tag=' + tag + '&category=' + category)
              .then(res => {
                  this.posts = res.data;
                  //this.post.body = Marked(this.post.body)
                  console.log(res.data)
              })
          }
    }
}

</script>
<style>
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
