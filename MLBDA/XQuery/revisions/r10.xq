<reuslt>
{for $title in distinct-values(//prices/book/title)
let $prix := min(//prices/book[title = $title]/price)
return
  <livre t='{$title}'>
    {$prix}
  </livre>
  
}</reuslt>