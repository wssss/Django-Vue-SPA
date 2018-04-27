<template>
    <nav class="pagination_align">
        <ul class="pagination" v-if="paginationTotal">
            <li @click="pageUp(0)" class="pagination_page" :class="startDisabled ? 'disabled' : ''">首页</li>
            <li @click="pageUp(1)" class="pagination_page" :class="startDisabled ? 'disabled' : ''">上一页</li>
            <li class="pagination_page" :class="item == paginationCurrentPage ? 'pagination_page_active' : ''"
                v-for="item in paginationLength" :key="item" @click="jump(item)">
                {{item}}
            </li>
            <li @click="pageDown(1)" class="pagination_page" :class="endDisabled ? 'disabled' : ''">下一页</li>
            <li @click="pageDown(0)" class="pagination_page pagination_page_right" :class="endDisabled ? 'disabled' : ''">尾页</li>
            <!-- <li><a>共<i>{{}}</i>页</a></li> -->
        </ul>
    </nav>
</template>
<script>
export default {
    props:['total', 'size', 'page', 'change', 'isUrl'],
    data(){
        return {
            paginationTotal:this.total, // 总条目数
            paginationSize: this.size ? this.size : 10, //每页显示多少个
            paginationLength: [],
            paginationCurrentPage: this.page ? this.page : 1,//当前页数默认1
            paginationPage: 0, // 可分页数
            startDisabled: true,
            endDisabled: true,
            pageChange: this.change,
            pageIsUrl:this.isUrl ? true:false //是否开启修改url
        }
    },
    methods:{
        jump(item){
            this.paginationCurrentPage = item;
            this.pagers();
            this.pageChange(this.paginationCurrentPage);
        },
        pagers(){
            this.paginationPage = Math.ceil(this.paginationTotal / this.paginationSize)

            if(this.pageIsUrl){
                this.$router.replace({
                    path:this.$route.path,
                    query:{
                        page: this.paginationCurrentPage
                    }
                })
            };

            //是否可以点击上一页
            this.startDisabled = this.paginationCurrentPage != 1 ? false : true;
            //是否可以点击下一页
            this.endDisabled = this.paginationCurrentPage != this.paginationPage ? false : true;

            if(this.paginationPage == 0){
                this.endDisabled == true
            }

            //重置
            this.paginationLength = [];
            //开始页码
            let start = this.paginationCurrentPage - 4 > 1 ? this.paginationCurrentPage - 4 : 1;
            let interval = this.paginationCurrentPage - start;
            //最多9个页码，总页码减去interval得到end 要显示的熟料 + 
            let end = (9 - interval) < this.paginationPage ? (9 - interval) : this.paginationPage;
            //最末页码减开始页码小于8
            if((end-start) != 8){
                //最末页码加上不足9页的数量，熟料不得大于总页数
                end = (end + (end - start)) < this.paginationPage ? end + (8 - (end - start)) : this.paginationPage;
                //最末页码加上但是还不够9页，进行开始页码追加，开始页码不得小于1
                if((end - start) != 8){
                    start = (end - 8) > 1 ? (end - 8) : 1;
                }
                for(let i = start; i <= end; i++){
                    this.paginationLength.push(i);
                }
            }
        },
        pageUp(state){
            if(this.startDisabled) return;
            if(this.paginationCurrentPage - 1 != 0 && state == 1){
                this.jump(this.paginationCurrentPage - 1);
            }else{
                this.jump(1)
            }
        },
        pageDown(state){
            if(this.end) return;
            if(this.paginationCurrentPage + 1 != this.paginationPage && state == 1){
                this.jump(this.paginationCurrentPage + 1);
            }else{
                this.jump(this.paginationPage);
            }
        },// state = 1 是下一页，state = 0 是尾页
        pageCurrentChange(){
            this.pageChange(this.paginationCurrentPage);
            this.pagers();
        }
    },
    created(){
        this.pageCurrentChange();
    },
    watch:{
        total: function(val, oldVal){
            this.paginationTotal = val;
            this.pagers();
        },
        page: function(val, oldVal){
            this.paginationCurrentPage = val;
            this.pagers()
        }
    }
}
</script>

<style scoped>
  .pagination_align{
    text-align: center
  }
  .pagination {
    color: #48576a;
    font-size: 12px;
    display: inline-block;
    user-select: none;
  }
  .pagination_page {
    padding: 0 4px;
    border: 1px solid #d1dbe5;
    border-right: 0;
    background: #fff;
    font-size: 13px;
    min-width: 28px;
    height: 28px;
    line-height: 28px;
    cursor: pointer;
    box-sizing: border-box;
    text-align: center;
    float: left;
  }
  .pagination_page_right {
    border-right: 1px solid #d1dbe5;
  }
  .pagination_page:hover {
    color: #20a0ff;
  }
  .disabled {
    color: #e4e4e4 !important;
    background-color: #fff;
    cursor: not-allowed;
  }
  .pagination_page_active {
    border-color: #20a0ff;
    background-color: #20a0ff;
    color: #fff !important;;
    cursor: default;
  }
</style>